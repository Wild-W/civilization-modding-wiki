---
tags:
- EffectType
title: EFFECT_ADJUST_ALL_DISTRICTS_PRODUCTION
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_ALL_DISTRICTS_PRODUCTION
>
> * Class: `CITIES`
> * Parameters:
>	* Amount `Integer`
>	* NotSpecialty `Unknown`

## Samples

```SQL {title="TRAIT_INTERCONTINENTAL_DISTRICT_PRODUCTION"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"TRAIT_INTERCONTINENTAL_DISTRICT_PRODUCTION",
		"MODIFIER_PLAYER_CITIES_ADJUST_ALL_DISTRICTS_PRODUCTION",
		"CITY_NOT_OWNER_CAPITAL_CONTINENT_REQUIREMENTS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_INTERCONTINENTAL_DISTRICT_PRODUCTION",
		"Amount",
		25
	);
	
```


```SQL {title="POLICY_CULTURE_INDUSTRY_GA_PRODUCTION_DISTRICT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"POLICY_CULTURE_INDUSTRY_GA_PRODUCTION_DISTRICT",
		"MODIFIER_PLAYER_CITIES_ADJUST_ALL_DISTRICTS_PRODUCTION"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"POLICY_CULTURE_INDUSTRY_GA_PRODUCTION_DISTRICT",
		"Amount",
		25
	),
	(
		"POLICY_CULTURE_INDUSTRY_GA_PRODUCTION_DISTRICT",
		"NotSpecialty",
		1
	);
	
```

