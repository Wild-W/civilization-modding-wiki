---
tags:
- EffectType
title: EFFECT_ADJUST_IMPROVEMENT_GOODY_HUT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_IMPROVEMENT_GOODY_HUT
>
> * Class: `PLAYERS`
> * Parameters:
>	* GoodyHutImprovementType `String`
>		* [Improvements.ImprovementType]
>	* ImprovementType `String`
>		* [Improvements.ImprovementType]

## Samples

```SQL {title="TRAIT_BARBARIAN_CAMP_GOODY"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_BARBARIAN_CAMP_GOODY",
		"MODIFIER_PLAYER_ADJUST_IMPROVEMENT_GOODY_HUT"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_BARBARIAN_CAMP_GOODY",
		"GoodyHutImprovementType",
		"IMPROVEMENT_GOODY_HUT"
	),
	(
		"TRAIT_BARBARIAN_CAMP_GOODY",
		"ImprovementType",
		"IMPROVEMENT_BARBARIAN_CAMP"
	);
	
```

