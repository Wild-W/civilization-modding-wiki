---
tags:
- EffectType
title: EFFECT_ADJUST_UNIT_AGAINST_DISTRICT_COMBAT_BONUS
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_UNIT_AGAINST_DISTRICT_COMBAT_BONUS
>
> * Class: `UNITS`
> * Parameters:
>	* Amount `Integer`

## Samples
```SQL {title="SERASKER_ADJUST_GOVERNOR_COMBAT_DISTRICT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"SERASKER_ADJUST_GOVERNOR_COMBAT_DISTRICT",
		"MODIFIER_GOVERNOR_ADJUST_DISTRICT_COMBAT_BONUS",
		"PLOT_10_TILES_AWAY_MAX_REQUIREMENTS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"SERASKER_ADJUST_GOVERNOR_COMBAT_DISTRICT",
		"Amount",
		10
	);
	
```

