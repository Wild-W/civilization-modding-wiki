---
tags:
- EffectType
title: EFFECT_ADJUST_RELIGIOUS_SPREAD_STRENGTH
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_RELIGIOUS_SPREAD_STRENGTH
>
> * Class: `PLAYERS`
> * Parameters:
>	* EnhancingTechType `String`
>		* [Technologies.TechnologyType]
>	* SpreadMultiplier `Integer`
>	* TechEnabledSpreadMultiplier `Integer`

## Samples
```SQL {title="SCRIPTURE_SPEAD_STRENGTH"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"SCRIPTURE_SPEAD_STRENGTH",
		"MODIFIER_PLAYER_RELIGION_ADJUST_RELIGIOUS_SPREAD_STRENGTH"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"SCRIPTURE_SPEAD_STRENGTH",
		"EnhancingTechType",
		"TECH_PRINTING"
	),
	(
		"SCRIPTURE_SPEAD_STRENGTH",
		"SpreadMultiplier",
		25
	),
	(
		"SCRIPTURE_SPEAD_STRENGTH",
		"TechEnabledSpreadMultiplier",
		25
	);
	
```

