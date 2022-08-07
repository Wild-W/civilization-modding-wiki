---
tags:
- EffectType
title: EFFECT_DIPLOMACY_CULTURAL_ID
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_DIPLOMACY_CULTURAL_ID
>
> * Class: `PLAYERS`
> * Parameters:
>	* CityGainLowerBound `Integer`
>	* CityGainUpperBound `Integer`
>	* ScorePerCity `Integer`
>	* SimpleModifierDescription `String`
>	* StatementKey `String`

## Samples

```SQL {title="AGENDA_SPIRIT_OF_TUCAPEL_GAINING_CITIES"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		OwnerRequirementSetId,
		SubjectRequirementSetId
	)
VALUES
	(
		"AGENDA_SPIRIT_OF_TUCAPEL_GAINING_CITIES",
		"MODIFIER_PLAYER_DIPLOMACY_AGENDA_SPIRIT_OF_TUCAPEL",
		"ON_TURN_STARTED",
		"PLAYER_IS_MAJOR_CIV_KNOWN_10_TURNS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"AGENDA_SPIRIT_OF_TUCAPEL_GAINING_CITIES",
		"CityGainLowerBound",
		0
	),
	(
		"AGENDA_SPIRIT_OF_TUCAPEL_GAINING_CITIES",
		"CityGainUpperBound",
		3
	),
	(
		"AGENDA_SPIRIT_OF_TUCAPEL_GAINING_CITIES",
		"ScorePerCity",
		3
	),
	(
		"AGENDA_SPIRIT_OF_TUCAPEL_GAINING_CITIES",
		"SimpleModifierDescription",
		"LOC_DIPLO_MODIFIER_SPIRIT_OF_TUCAPEL_GAINING_CITIES"
	),
	(
		"AGENDA_SPIRIT_OF_TUCAPEL_GAINING_CITIES",
		"StatementKey",
		"LOC_DIPLO_KUDO_LEADER_LAUTARO_REASON_ANY"
	);
	
```

