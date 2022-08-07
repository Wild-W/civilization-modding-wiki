---
tags:
- EffectType
title: EFFECT_ADJUST_CITY_TOURISM
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_CITY_TOURISM
>
> * Class: `CITIES`
> * Parameters:
>	* BoostsWonders `Boolean`
>	* GreatWorkObjectType `String`
>		* [GreatWorkObjectTypes.GreatWorkObjectType]
>	* ImprovementType `String`
>		* [Improvements.ImprovementType]
>	* Religious `Boolean`
>	* ScalingFactor `Integer`

## Samples

```SQL {title="TRAIT_WONDER_DOUBLETOURISM"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_WONDER_DOUBLETOURISM",
		"MODIFIER_PLAYER_CITIES_ADJUST_TOURISM"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_WONDER_DOUBLETOURISM",
		"BoostsWonders",
		1
	),
	(
		"TRAIT_WONDER_DOUBLETOURISM",
		"ScalingFactor",
		200
	);
	
```


```SQL {title="RELIQUARIES_RELIC_TOURISM_MODIFIER"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"RELIQUARIES_RELIC_TOURISM_MODIFIER",
		"MODIFIER_SINGLE_CITY_ADJUST_TOURISM"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"RELIQUARIES_RELIC_TOURISM_MODIFIER",
		"GreatWorkObjectType",
		"GREATWORKOBJECT_RELIC"
	),
	(
		"RELIQUARIES_RELIC_TOURISM_MODIFIER",
		"ScalingFactor",
		300
	);
	
```


```SQL {title="CRISTOREDENTOR_BEACHTOURISM"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"CRISTOREDENTOR_BEACHTOURISM",
		"MODIFIER_PLAYER_CITIES_ADJUST_TOURISM"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"CRISTOREDENTOR_BEACHTOURISM",
		"ImprovementType",
		"IMPROVEMENT_BEACH_RESORT"
	),
	(
		"CRISTOREDENTOR_BEACHTOURISM",
		"ScalingFactor",
		200
	);
	
```


```SQL {title="STBASILS_ADDRELIGIOUSTOURISM"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"STBASILS_ADDRELIGIOUSTOURISM",
		"MODIFIER_SINGLE_CITY_ADJUST_TOURISM"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"STBASILS_ADDRELIGIOUSTOURISM",
		"Religious",
		1
	),
	(
		"STBASILS_ADDRELIGIOUSTOURISM",
		"ScalingFactor",
		200
	);
	
```

