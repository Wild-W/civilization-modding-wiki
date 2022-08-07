---
tags:
- EffectType
title: EFFECT_ADD_DIPLOMATIC_YIELD_MODIFIER
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADD_DIPLOMATIC_YIELD_MODIFIER
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`
>	* DiplomaticYieldSource `String`
>		* CITY_CAPTURED>		  LIBERATION>		  LIBERATION_WAR_INITIATED>		  PROTECTORATE_WAR_INITIATED>		  SURPRISE_WAR_INITIATED>		  TERRITORIAL_EXPANSION_WAR_INITIATED>		  WAR_DECLARATION_INITIATED>		  WAR_DECLARATION_RECEIVED
>	* StackWithOtherDiploYieldModifiers `Boolean`
>	* TurnsActive `Integer`
>	* YieldType `String`
>		* [Yields.YieldType]

## Samples

```SQL {title="TRAIT_CITADELCIVILIZATION_DEFENSIVE_PRODUCTION"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"TRAIT_CITADELCIVILIZATION_DEFENSIVE_PRODUCTION",
		"MODIFIER_PLAYER_ADD_DIPLOMATIC_YIELD_MODIFIER"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"TRAIT_CITADELCIVILIZATION_DEFENSIVE_PRODUCTION",
		"Amount",
		100
	),
	(
		"TRAIT_CITADELCIVILIZATION_DEFENSIVE_PRODUCTION",
		"DiplomaticYieldSource",
		"WAR_DECLARATION_RECEIVED"
	),
	(
		"TRAIT_CITADELCIVILIZATION_DEFENSIVE_PRODUCTION",
		"TurnsActive",
		10
	),
	(
		"TRAIT_CITADELCIVILIZATION_DEFENSIVE_PRODUCTION",
		"YieldType",
		"YIELD_PRODUCTION"
	);
	
```


```SQL {title="GOV_PRODUCTION_BOOST_FROM_CAPTURE"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"GOV_PRODUCTION_BOOST_FROM_CAPTURE",
		"MODIFIER_PLAYER_ADD_DIPLOMATIC_YIELD_MODIFIER"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"GOV_PRODUCTION_BOOST_FROM_CAPTURE",
		"Amount",
		20
	),
	(
		"GOV_PRODUCTION_BOOST_FROM_CAPTURE",
		"DiplomaticYieldSource",
		"CITY_CAPTURED"
	),
	(
		"GOV_PRODUCTION_BOOST_FROM_CAPTURE",
		"StackWithOtherDiploYieldModifiers",
		1
	),
	(
		"GOV_PRODUCTION_BOOST_FROM_CAPTURE",
		"TurnsActive",
		5
	),
	(
		"GOV_PRODUCTION_BOOST_FROM_CAPTURE",
		"YieldType",
		"YIELD_PRODUCTION"
	);
	
```

