---
tags:
- EffectType
title: EFFECT_GRANT_FREE_RESOURCE_VISIBILITY
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_GRANT_FREE_RESOURCE_VISIBILITY
>
> * Class: `PLAYERS`
> * Parameters:
>	* ResourceType `String`
>		* [Resources.ResourceType]

## Samples
```SQL {title="GREATPERSON_REVEAL_OIL"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		RunOnce,
		Permanent
	)
VALUES
	(
		"GREATPERSON_REVEAL_OIL",
		"MODIFIER_PLAYER_GRANT_FREE_RESOURCE_VISIBILITY",
		1,
		1
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"GREATPERSON_REVEAL_OIL",
		"ResourceType",
		"RESOURCE_OIL"
	);
	
```

