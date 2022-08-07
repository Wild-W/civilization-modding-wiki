---
tags:
- EffectType
title: EFFECT_ATTACH_MODIFIER_TO_PLAYERTYPE
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ATTACH_MODIFIER_TO_PLAYERTYPE
>
> * Class: `ANY`
> * Parameters:
>	* ModifierId `String`

## Samples

```SQL {title="APPLY_INCREASED_DIPLO_VP_TO_PLAYER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"APPLY_INCREASED_DIPLO_VP_TO_PLAYER",
		"MODIFIER_CONGRESS_ATTACH_MODIFIER_TO_PLAYERTYPE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"APPLY_INCREASED_DIPLO_VP_TO_PLAYER",
		"ModifierId",
		"ADD_DIPLOMATIC_VICTORY_POINTS"
	);
	
```

