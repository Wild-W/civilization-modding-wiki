---
tags:
- EffectType
title: EFFECT_DIPLOMACY_AGENDA_SIMON_BOLIVAR
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_DIPLOMACY_AGENDA_SIMON_BOLIVAR
>
> * Class: `PLAYERS`
> * Parameters:
>	* MinPromotedUnits `Integer`
>	* NumSteps `Integer`
>	* PercentageDifferencePerStep `Integer`
>	* ScorePerStep `Integer`
>	* SimpleModifierDescription `String`
>	* StatementKey `String`

## Samples

```SQL {title="AGENDA_MODIFIER_SIMON_BOLIVAR"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		OwnerRequirementSetId,
		SubjectRequirementSetId
	)
VALUES
	(
		"AGENDA_MODIFIER_SIMON_BOLIVAR",
		"MODIFIER_PLAYER_DIPLOMACY_AGENDA_SIMON_BOLIVAR",
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
		"AGENDA_MODIFIER_SIMON_BOLIVAR",
		"MinPromotedUnits",
		5
	),
	(
		"AGENDA_MODIFIER_SIMON_BOLIVAR",
		"NumSteps",
		4
	),
	(
		"AGENDA_MODIFIER_SIMON_BOLIVAR",
		"PercentageDifferencePerStep",
		10
	),
	(
		"AGENDA_MODIFIER_SIMON_BOLIVAR",
		"ScorePerStep",
		3
	),
	(
		"AGENDA_MODIFIER_SIMON_BOLIVAR",
		"SimpleModifierDescription",
		"LOC_DIPLO_MODIFIER_AGENDA_SIMON_BOLIVAR"
	),
	(
		"AGENDA_MODIFIER_SIMON_BOLIVAR",
		"StatementKey",
		"LOC_DIPLO_KUDO_EXIT_LEADER_SIMON_BOLIVAR_ANY"
	);
	
```

