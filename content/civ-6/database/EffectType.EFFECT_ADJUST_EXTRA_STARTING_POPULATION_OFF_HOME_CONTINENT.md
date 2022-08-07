---
tags:
- EffectType
title: EFFECT_ADJUST_EXTRA_STARTING_POPULATION_OFF_HOME_CONTINENT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_EXTRA_STARTING_POPULATION_OFF_HOME_CONTINENT
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`

## Samples

```SQL {title="COMMEMORATION_EXPLORATION_GA_NEW_CITY_POPULATION"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		OwnerRequirementSetId
	)
VALUES
	(
		"COMMEMORATION_EXPLORATION_GA_NEW_CITY_POPULATION",
		"MODIFIER_PLAYER_ADJUST_EXTRA_STARTING_POPULATION_OFF_HOME_CONTINENT",
		"PLAYER_HAS_GOLDEN_AGE"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"COMMEMORATION_EXPLORATION_GA_NEW_CITY_POPULATION",
		"Amount",
		3
	);
	
```

