---
tags:
- EffectType
title: EFFECT_ATTACH_MODIFIER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ATTACH_MODIFIER
>
> * Class: `ANY`
> * Parameters:
>	* ModifierId `String`

## Samples

```SQL {title="MONUMENT_TO_THE_GODS_ANCIENTCLASSICALWONDER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"MONUMENT_TO_THE_GODS_ANCIENTCLASSICALWONDER",
		"MODIFIER_ALL_PLAYERS_ATTACH_MODIFIER",
		"PLAYER_HAS_PANTHEON_REQUIREMENTS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"MONUMENT_TO_THE_GODS_ANCIENTCLASSICALWONDER",
		"ModifierId",
		"MONUMENT_TO_THE_GODS_ANCIENTCLASSICALWONDER_MODIFIER"
	);
	
```

